---
title: SSLContext.createSSLEngine()
permalink: /Java/SSLContext/createSSLEngine/
date: 2021-01-11
key: Java.S.SSLContext
category: Java
tags: ['java se', 'javax.net.ssl', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SSLContext.metodos valor="createSSLEngine" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public final SSLEngine createSSLEngine()
public final SSLEngine createSSLEngine(String peerHost, int peerPort)
~~~

## Parámetros
* **String peerHost**,  {% include w3api/param_description.html metodo=_dato parametro="String peerHost" %}
* **int peerPort**,  {% include w3api/param_description.html metodo=_dato parametro="int peerPort" %}

## Excepciones
[IllegalStateException](/Java/IllegalStateException/), [UnsupportedOperationException](/Java/UnsupportedOperationException/)

## Clase Padre
[SSLContext](/Java/SSLContext/)

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
