---
title: GSSManager.createName()
permalink: /Java/GSSManager/createName/
date: 2021-01-11
key: Java.G.GSSManager
category: Java
tags: ['java se', 'org.ietf.jgss', 'java.security.jgss', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.G.GSSManager.metodos valor="createName" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract GSSName createName(byte[] name, Oid nameType) throws GSSException
public abstract GSSName createName(byte[] name, Oid nameType, Oid mech) throws GSSException
public abstract GSSName createName(String nameStr, Oid nameType) throws GSSException
public abstract GSSName createName(String nameStr, Oid nameType, Oid mech) throws GSSException
~~~

## Parámetros
* **byte[] name**,  {% include w3api/param_description.html metodo=_dato parametro="byte[] name" %}
* **String nameStr**,  {% include w3api/param_description.html metodo=_dato parametro="String nameStr" %}
* **Oid mech**,  {% include w3api/param_description.html metodo=_dato parametro="Oid mech" %}
* **Oid nameType**,  {% include w3api/param_description.html metodo=_dato parametro="Oid nameType" %}

## Excepciones
[GSSException](/Java/GSSException/)

## Clase Padre
[GSSManager](/Java/GSSManager/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
