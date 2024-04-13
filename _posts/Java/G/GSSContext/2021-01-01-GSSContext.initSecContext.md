---
title: GSSContext.initSecContext()
permalink: /Java/GSSContext/initSecContext/
date: 2021-01-11
key: Java.G.GSSContext
category: Java
tags: ['java se', 'org.ietf.jgss', 'java.security.jgss', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.G.GSSContext.metodos valor="initSecContext" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
byte[] initSecContext(byte[] inputBuf, int offset, int len) throws GSSException
int initSecContext(InputStream inStream, OutputStream outStream) throws GSSException
~~~

## Parámetros
* **InputStream inStream**,  {% include w3api/param_description.html metodo=_dato parametro="InputStream inStream" %}
* **int len**,  {% include w3api/param_description.html metodo=_dato parametro="int len" %}
* **byte[] inputBuf**,  {% include w3api/param_description.html metodo=_dato parametro="byte[] inputBuf" %}
* **int offset**,  {% include w3api/param_description.html metodo=_dato parametro="int offset" %}
* **OutputStream outStream**,  {% include w3api/param_description.html metodo=_dato parametro="OutputStream outStream" %}

## Excepciones
[GSSException](/Java/GSSException/)

## Clase Padre
[GSSContext](/Java/GSSContext/)

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
