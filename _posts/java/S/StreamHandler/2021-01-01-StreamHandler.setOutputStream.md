---
title: StreamHandler.setOutputStream()
permalink: Java/StreamHandler/setOutputStream
date: 2021-01-11
key: JavaJava.S.StreamHandler
category: java
tags: ['java se', 'java.util.logging', 'java.logging', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.StreamHandler.metodos valor="setOutputStream" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected void setOutputStream(OutputStream out) throws SecurityException
~~~

## Parámetros
* **OutputStream out**,  {% include w3api/param_description.html metodo=_dato parametro="OutputStream out" %}

## Excepciones
[SecurityException](/Java/SecurityException/)

## Clase Padre
[StreamHandler](/Java/StreamHandler/)

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
