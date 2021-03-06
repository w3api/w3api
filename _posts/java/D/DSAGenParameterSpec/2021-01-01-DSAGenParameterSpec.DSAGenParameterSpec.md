---
title: DSAGenParameterSpec.DSAGenParameterSpec()
permalink: /Java/DSAGenParameterSpec/DSAGenParameterSpec/
date: 2021-01-11
key: Java.D.DSAGenParameterSpec
category: Java
tags: ['java se', 'java.security.spec', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DSAGenParameterSpec.constructores valor="DSAGenParameterSpec" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public DSAGenParameterSpec(int primePLen, int subprimeQLen)
public DSAGenParameterSpec(int primePLen, int subprimeQLen, int seedLen)
~~~

## Parámetros
* **int subprimeQLen**,  {% include w3api/param_description.html metodo=_dato parametro="int subprimeQLen" %}
* **int seedLen**,  {% include w3api/param_description.html metodo=_dato parametro="int seedLen" %}
* **int primePLen**,  {% include w3api/param_description.html metodo=_dato parametro="int primePLen" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[DSAGenParameterSpec](/Java/DSAGenParameterSpec/)

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
