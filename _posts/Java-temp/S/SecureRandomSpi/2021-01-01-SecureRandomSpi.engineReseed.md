---
title: SecureRandomSpi.engineReseed()
permalink: /Java/SecureRandomSpi/engineReseed/
date: 2021-01-11
key: Java.S.SecureRandomSpi
category: Java
tags: ['java se', 'java.security', 'java.base', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SecureRandomSpi.metodos valor="engineReseed" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected void engineReseed(SecureRandomParameters params)
~~~

## Parámetros
* **SecureRandomParameters params**,  {% include w3api/param_description.html metodo=_dato parametro="SecureRandomParameters params" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [UnsupportedOperationException](/Java/UnsupportedOperationException/)

## Clase Padre
[SecureRandomSpi](/Java/SecureRandomSpi/)

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
