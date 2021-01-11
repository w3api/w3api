---
title: AlgorithmParameters.AlgorithmParameters()
permalink: Java/AlgorithmParameters/AlgorithmParameters
date: 2021-01-10
key: JavaJava.A.AlgorithmParameters
category: java
tags: ['java se', 'java.security', 'java.base', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AlgorithmParameters.constructores valor="AlgorithmParameters" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected AlgorithmParameters(AlgorithmParametersSpi paramSpi, Provider provider, String algorithm)
~~~

## Parámetros
* **String algorithm**,  {% include w3api/param_description.html metodo=_dato parametro="String algorithm" %}
* **AlgorithmParametersSpi paramSpi**,  {% include w3api/param_description.html metodo=_dato parametro="AlgorithmParametersSpi paramSpi" %}
* **Provider provider**,  {% include w3api/param_description.html metodo=_dato parametro="Provider provider" %}

## Clase Padre
[AlgorithmParameters](/Java/AlgorithmParameters/)

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
