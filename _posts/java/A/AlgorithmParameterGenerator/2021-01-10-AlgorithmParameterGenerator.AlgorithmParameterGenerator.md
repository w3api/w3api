---
title: AlgorithmParameterGenerator.AlgorithmParameterGenerator()
permalink: Java/AlgorithmParameterGenerator/AlgorithmParameterGenerator
date: 2021-01-10
key: JavaJava.A.AlgorithmParameterGenerator
category: java
tags: ['java se', 'java.security', 'java.base', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AlgorithmParameterGenerator.constructores valor="AlgorithmParameterGenerator" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected AlgorithmParameterGenerator(AlgorithmParameterGeneratorSpi paramGenSpi, Provider provider, String algorithm)
~~~

## Parámetros
* **String algorithm**,  {% include w3api/param_description.html metodo=_dato parametro="String algorithm" %}
* **AlgorithmParameterGeneratorSpi paramGenSpi**,  {% include w3api/param_description.html metodo=_dato parametro="AlgorithmParameterGeneratorSpi paramGenSpi" %}
* **Provider provider**,  {% include w3api/param_description.html metodo=_dato parametro="Provider provider" %}

## Clase Padre
[AlgorithmParameterGenerator](/Java/AlgorithmParameterGenerator/)

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
