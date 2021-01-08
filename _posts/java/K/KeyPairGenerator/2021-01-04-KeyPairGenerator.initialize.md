---
title: KeyPairGenerator.initialize()
permalink: Java/KeyPairGenerator/initialize
date: 2021-01-04
key: JavaJava.K.KeyPairGenerator
category: java
tags: ['java se', 'java.security', 'java.base', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.K.KeyPairGenerator.metodos valor="initialize" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void initialize(int keysize)
public void initialize(int keysize, SecureRandom random)
public void initialize(AlgorithmParameterSpec params) throws InvalidAlgorithmParameterException
public void initialize(AlgorithmParameterSpec params, SecureRandom random) throws InvalidAlgorithmParameterException
~~~

## Parámetros
* **SecureRandom random**,  {% include w3api/param_description.html metodo=_data parametro="SecureRandom random" %}
* **AlgorithmParameterSpec params**,  {% include w3api/param_description.html metodo=_data parametro="AlgorithmParameterSpec params" %}
* **int keysize**,  {% include w3api/param_description.html metodo=_data parametro="int keysize" %}

## Excepciones
[InvalidAlgorithmParameterException](/Java/InvalidAlgorithmParameterException/), [InvalidParameterException](/Java/InvalidParameterException/)

## Clase Padre
[KeyPairGenerator](/Java/KeyPairGenerator/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.K.KeyPairGenerator.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
