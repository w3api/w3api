---
title: AlgorithmParameterGenerator.getInstance()
permalink: Java/AlgorithmParameterGenerator/getInstance
date: 2021-01-04
key: JavaJava.A.AlgorithmParameterGenerator
category: java
tags: ['java se', 'java.security', 'java.base', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AlgorithmParameterGenerator.metodos valor="getInstance" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static AlgorithmParameterGenerator getInstance(String algorithm) throws NoSuchAlgorithmException
public static AlgorithmParameterGenerator getInstance(String algorithm, String provider) throws NoSuchAlgorithmException, NoSuchProviderException
public static AlgorithmParameterGenerator getInstance(String algorithm, Provider provider) throws NoSuchAlgorithmException
~~~

## Parámetros
* **String algorithm**,  {% include w3api/param_description.html metodo=_data parametro="String algorithm" %}
* **String provider**,  {% include w3api/param_description.html metodo=_data parametro="String provider" %}
* **Provider provider**,  {% include w3api/param_description.html metodo=_data parametro="Provider provider" %}

## Excepciones
[NoSuchAlgorithmException](/Java/NoSuchAlgorithmException/), [NullPointerException](/Java/NullPointerException/), [NoSuchProviderException](/Java/NoSuchProviderException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

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
