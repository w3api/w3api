---
title: AlgorithmParameters.getInstance()
permalink: Java/AlgorithmParameters/getInstance
date: 2021-01-04
key: JavaJava.A.AlgorithmParameters
category: java
tags: ['java se', 'java.security', 'java.base', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AlgorithmParameters.metodos valor="getInstance" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static AlgorithmParameters getInstance(String algorithm) throws NoSuchAlgorithmException
public static AlgorithmParameters getInstance(String algorithm, String provider) throws NoSuchAlgorithmException, NoSuchProviderException
public static AlgorithmParameters getInstance(String algorithm, Provider provider) throws NoSuchAlgorithmException
~~~

## Parámetros
* **String algorithm**,  {% include w3api/param_description.html metodo=_data parametro="String algorithm" %}
* **String provider**,  {% include w3api/param_description.html metodo=_data parametro="String provider" %}
* **Provider provider**,  {% include w3api/param_description.html metodo=_data parametro="Provider provider" %}

## Excepciones
[NoSuchAlgorithmException](/Java/NoSuchAlgorithmException/), [NullPointerException](/Java/NullPointerException/), [NoSuchProviderException](/Java/NoSuchProviderException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[AlgorithmParameters](/Java/AlgorithmParameters/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.A.AlgorithmParameters.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
