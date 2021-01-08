---
title: SSLContext.createSSLEngine()
permalink: Java/SSLContext/createSSLEngine
date: 2021-01-04
key: JavaJava.S.SSLContext
category: java
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
* **String peerHost**,  {% include w3api/param_description.html metodo=_data parametro="String peerHost" %}
* **int peerPort**,  {% include w3api/param_description.html metodo=_data parametro="int peerPort" %}

## Excepciones
[UnsupportedOperationException](/Java/UnsupportedOperationException/), [IllegalStateException](/Java/IllegalStateException/)

## Clase Padre
[SSLContext](/Java/SSLContext/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.SSLContext.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
