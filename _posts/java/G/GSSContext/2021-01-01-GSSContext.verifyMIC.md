---
title: GSSContext.verifyMIC()
permalink: Java/GSSContext/verifyMIC
date: 2021-01-11
key: JavaJava.G.GSSContext
category: java
tags: ['java se', 'org.ietf.jgss', 'java.security.jgss', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.G.GSSContext.metodos valor="verifyMIC" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void verifyMIC(byte[] inToken, int tokOffset, int tokLen, byte[] inMsg, int msgOffset, int msgLen, MessageProp msgProp) throws GSSException
void verifyMIC(InputStream tokStream, InputStream msgStream, MessageProp msgProp) throws GSSException
~~~

## Parámetros
* **int msgLen**,  {% include w3api/param_description.html metodo=_dato parametro="int msgLen" %}
* **InputStream tokStream**,  {% include w3api/param_description.html metodo=_dato parametro="InputStream tokStream" %}
* **int tokLen**,  {% include w3api/param_description.html metodo=_dato parametro="int tokLen" %}
* **MessageProp msgProp**,  {% include w3api/param_description.html metodo=_dato parametro="MessageProp msgProp" %}
* **InputStream msgStream**,  {% include w3api/param_description.html metodo=_dato parametro="InputStream msgStream" %}
* **byte[] inToken**,  {% include w3api/param_description.html metodo=_dato parametro="byte[] inToken" %}
* **byte[] inMsg**,  {% include w3api/param_description.html metodo=_dato parametro="byte[] inMsg" %}
* **int msgOffset**,  {% include w3api/param_description.html metodo=_dato parametro="int msgOffset" %}
* **int tokOffset**,  {% include w3api/param_description.html metodo=_dato parametro="int tokOffset" %}

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
