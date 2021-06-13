---
title: PBEParameterSpec.PBEParameterSpec()
permalink: /Java/PBEParameterSpec/PBEParameterSpec/
date: 2021-01-11
key: Java.P.PBEParameterSpec
category: java
tags: ['java se', 'javax.crypto.spec', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.PBEParameterSpec.constructores valor="PBEParameterSpec" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public PBEParameterSpec(byte[] salt, int iterationCount)
public PBEParameterSpec(byte[] salt, int iterationCount, AlgorithmParameterSpec paramSpec)
~~~

## Parámetros
* **AlgorithmParameterSpec paramSpec**,  {% include w3api/param_description.html metodo=_dato parametro="AlgorithmParameterSpec paramSpec" %}
* **byte[] salt**,  {% include w3api/param_description.html metodo=_dato parametro="byte[] salt" %}
* **int iterationCount**,  {% include w3api/param_description.html metodo=_dato parametro="int iterationCount" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/)

## Clase Padre
[PBEParameterSpec](/Java/PBEParameterSpec/)

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
