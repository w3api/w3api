---
title: SSLContext.setDefault()
permalink: Java/SSLContext/setDefault
date: 2021-01-11
key: JavaJava.S.SSLContext
category: java
tags: ['java se', 'javax.net.ssl', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SSLContext.metodos valor="setDefault" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static void setDefault(SSLContext context)
~~~

## Parámetros
* **SSLContext context**,  {% include w3api/param_description.html metodo=_dato parametro="SSLContext context" %}

## Excepciones
[SecurityException](/Java/SecurityException/), [NullPointerException](/Java/NullPointerException/)

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
