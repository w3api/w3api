---
title: GSSManager.createContext()
permalink: Java/GSSManager/createContext
date: 2021-01-04
key: JavaJava.G.GSSManager
category: java
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
* **byte[] interProcessToken**,  {% include w3api/param_description.html metodo=_data parametro="byte[] interProcessToken" %}
* **Oid mech**,  {% include w3api/param_description.html metodo=_data parametro="Oid mech" %}
* **GSSName peer**,  {% include w3api/param_description.html metodo=_data parametro="GSSName peer" %}
* **GSSCredential myCred**,  {% include w3api/param_description.html metodo=_data parametro="GSSCredential myCred" %}
* **int lifetime**,  {% include w3api/param_description.html metodo=_data parametro="int lifetime" %}

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
