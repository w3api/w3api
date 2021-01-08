---
title: AlgorithmParameterGenerator.AlgorithmParameterGenerator()
permalink: Java/AlgorithmParameterGenerator/AlgorithmParameterGenerator
date: 2021-01-04
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
* **Provider provider**,  {% include w3api/param_description.html metodo=_data parametro="Provider provider" %}
* **String algorithm**,  {% include w3api/param_description.html metodo=_data parametro="String algorithm" %}
* **AlgorithmParameterGeneratorSpi paramGenSpi**,  {% include w3api/param_description.html metodo=_data parametro="AlgorithmParameterGeneratorSpi paramGenSpi" %}

## Clase Padre
[AlgorithmParameterGenerator](/Java/AlgorithmParameterGenerator/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.A.AlgorithmParameterGenerator.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
