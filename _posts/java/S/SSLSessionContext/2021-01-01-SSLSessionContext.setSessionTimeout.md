---
title: SSLSessionContext.setSessionTimeout()
permalink: /Java/SSLSessionContext/setSessionTimeout/
date: 2021-01-11
key: Java.S.SSLSessionContext
category: Java
tags: ['java se', 'javax.net.ssl', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SSLSessionContext.metodos valor="setSessionTimeout" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void setSessionTimeout(int seconds) throws IllegalArgumentException
~~~

## Parámetros
* **int seconds**,  {% include w3api/param_description.html metodo=_dato parametro="int seconds" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

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
