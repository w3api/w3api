---
title: GSSContext.acceptSecContext()
permalink: Java/GSSContext/acceptSecContext
date: 2021-01-04
key: JavaJava.G.GSSContext
category: java
tags: ['java se', 'org.ietf.jgss', 'java.security.jgss', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.G.GSSContext.metodos valor="acceptSecContext" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
byte[] acceptSecContext(byte[] inToken, int offset, int len) throws GSSException
void acceptSecContext(InputStream inStream, OutputStream outStream) throws GSSException
~~~

## Parámetros
* **byte[] inToken**,  {% include w3api/param_description.html metodo=_data parametro="byte[] inToken" %}
* **OutputStream outStream**,  {% include w3api/param_description.html metodo=_data parametro="OutputStream outStream" %}
* **InputStream inStream**,  {% include w3api/param_description.html metodo=_data parametro="InputStream inStream" %}
* **int len**,  {% include w3api/param_description.html metodo=_data parametro="int len" %}
* **int offset**,  {% include w3api/param_description.html metodo=_data parametro="int offset" %}

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
{%- for _ldc in site.data.Java.G.GSSContext.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
