---
title: SSLContextSpi.engineCreateSSLEngine()
permalink: Java/SSLContextSpi/engineCreateSSLEngine
date: 2021-01-11
key: JavaJava.S.SSLContextSpi
category: java
tags: ['java se', 'javax.net.ssl', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SSLContextSpi.metodos valor="engineCreateSSLEngine" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected abstract SSLEngine engineCreateSSLEngine()
protected abstract SSLEngine engineCreateSSLEngine(String host, int port)
~~~

## Parámetros
* **int port**,  {% include w3api/param_description.html metodo=_dato parametro="int port" %}
* **String host**,  {% include w3api/param_description.html metodo=_dato parametro="String host" %}

## Excepciones
[IllegalStateException](/Java/IllegalStateException/)

## Clase Padre
[SSLContextSpi](/Java/SSLContextSpi/)

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
