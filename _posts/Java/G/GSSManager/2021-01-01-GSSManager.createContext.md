---
title: GSSManager.createContext()
permalink: /Java/GSSManager/createContext/
date: 2021-01-11
key: Java.G.GSSManager
category: Java
tags: ['java se', 'org.ietf.jgss', 'java.security.jgss', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.G.GSSManager.metodos valor="createContext" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract GSSContext createContext(byte[] interProcessToken) throws GSSException
public abstract GSSContext createContext(GSSCredential myCred) throws GSSException
public abstract GSSContext createContext(GSSName peer, Oid mech, GSSCredential myCred, int lifetime) throws GSSException
~~~

## Parámetros
* **GSSName peer**,  {% include w3api/param_description.html metodo=_dato parametro="GSSName peer" %}
* **int lifetime**,  {% include w3api/param_description.html metodo=_dato parametro="int lifetime" %}
* **byte[] interProcessToken**,  {% include w3api/param_description.html metodo=_dato parametro="byte[] interProcessToken" %}
* **GSSCredential myCred**,  {% include w3api/param_description.html metodo=_dato parametro="GSSCredential myCred" %}
* **Oid mech**,  {% include w3api/param_description.html metodo=_dato parametro="Oid mech" %}

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
