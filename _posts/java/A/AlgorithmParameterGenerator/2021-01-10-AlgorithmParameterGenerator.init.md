---
title: AlgorithmParameterGenerator.init()
permalink: Java/AlgorithmParameterGenerator/init
date: 2021-01-10
key: JavaJava.A.AlgorithmParameterGenerator
category: java
tags: ['java se', 'java.security', 'java.base', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AlgorithmParameterGenerator.metodos valor="init" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public final void init(int size)
public final void init(int size, SecureRandom random)
public final void init(AlgorithmParameterSpec genParamSpec) throws InvalidAlgorithmParameterException
public final void init(AlgorithmParameterSpec genParamSpec, SecureRandom random) throws InvalidAlgorithmParameterException
~~~

## Parámetros
* **AlgorithmParameterSpec genParamSpec**,  {% include w3api/param_description.html metodo=_dato parametro="AlgorithmParameterSpec genParamSpec" %}
* **int size**,  {% include w3api/param_description.html metodo=_dato parametro="int size" %}
* **SecureRandom random**,  {% include w3api/param_description.html metodo=_dato parametro="SecureRandom random" %}

## Excepciones
[InvalidAlgorithmParameterException](/Java/InvalidAlgorithmParameterException/)

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
