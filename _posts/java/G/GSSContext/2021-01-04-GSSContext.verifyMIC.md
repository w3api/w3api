---
title: GSSContext.verifyMIC()
permalink: Java/GSSContext/verifyMIC
date: 2021-01-04
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
* **byte[] inToken**,  {% include w3api/param_description.html metodo=_data parametro="byte[] inToken" %}
* **int tokLen**,  {% include w3api/param_description.html metodo=_data parametro="int tokLen" %}
* **int msgLen**,  {% include w3api/param_description.html metodo=_data parametro="int msgLen" %}
* **InputStream msgStream**,  {% include w3api/param_description.html metodo=_data parametro="InputStream msgStream" %}
* **int msgOffset**,  {% include w3api/param_description.html metodo=_data parametro="int msgOffset" %}
* **int tokOffset**,  {% include w3api/param_description.html metodo=_data parametro="int tokOffset" %}
* **InputStream tokStream**,  {% include w3api/param_description.html metodo=_data parametro="InputStream tokStream" %}
* **MessageProp msgProp**,  {% include w3api/param_description.html metodo=_data parametro="MessageProp msgProp" %}
* **byte[] inMsg**,  {% include w3api/param_description.html metodo=_data parametro="byte[] inMsg" %}

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
