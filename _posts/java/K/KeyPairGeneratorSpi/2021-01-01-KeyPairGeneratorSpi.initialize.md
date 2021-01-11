---
title: KeyPairGeneratorSpi.initialize()
permalink: Java/KeyPairGeneratorSpi/initialize
date: 2021-01-11
key: JavaJava.K.KeyPairGeneratorSpi
category: java
tags: ['java se', 'java.security', 'java.base', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.K.KeyPairGeneratorSpi.metodos valor="initialize" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract void initialize(int keysize, SecureRandom random)
public void initialize(AlgorithmParameterSpec params, SecureRandom random) throws InvalidAlgorithmParameterException
~~~

## Parámetros
* **int keysize**,  {% include w3api/param_description.html metodo=_dato parametro="int keysize" %}
* **AlgorithmParameterSpec params**,  {% include w3api/param_description.html metodo=_dato parametro="AlgorithmParameterSpec params" %}
* **SecureRandom random**,  {% include w3api/param_description.html metodo=_dato parametro="SecureRandom random" %}

## Excepciones
[InvalidParameterException](/Java/InvalidParameterException/), [InvalidAlgorithmParameterException](/Java/InvalidAlgorithmParameterException/)

## Clase Padre
[KeyPairGeneratorSpi](/Java/KeyPairGeneratorSpi/)

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
