---
title: SSLSessionContext.getSession()
permalink: Java/SSLSessionContext/getSession
date: 2021-01-11
key: JavaJava.S.SSLSessionContext
category: java
tags: ['java se', 'javax.net.ssl', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SSLSessionContext.metodos valor="getSession" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
SSLSession getSession(byte[] sessionId)
~~~

## Parámetros
* **byte[] sessionId**,  {% include w3api/param_description.html metodo=_dato parametro="byte[] sessionId" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/)

## Clase Padre
[SSLSessionContext](/Java/SSLSessionContext/)

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
