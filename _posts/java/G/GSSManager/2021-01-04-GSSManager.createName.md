---
title: GSSManager.createName()
permalink: Java/GSSManager/createName
date: 2021-01-04
key: JavaJava.G.GSSManager
category: java
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
* **String nameStr**,  {% include w3api/param_description.html metodo=_data parametro="String nameStr" %}
* **byte[] name**,  {% include w3api/param_description.html metodo=_data parametro="byte[] name" %}
* **Oid nameType**,  {% include w3api/param_description.html metodo=_data parametro="Oid nameType" %}
* **Oid mech**,  {% include w3api/param_description.html metodo=_data parametro="Oid mech" %}

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
{%- for _ldc in site.data.Java.G.GSSManager.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
