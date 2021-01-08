---
title: KeyGenerator.init()
permalink: Java/KeyGenerator/init
date: 2021-01-04
key: JavaJava.K.KeyGenerator
category: java
tags: ['java se', 'javax.crypto', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.K.KeyGenerator.metodos valor="init" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public final void init(int keysize)
public final void init(int keysize, SecureRandom random)
public final void init(SecureRandom random)
public final void init(AlgorithmParameterSpec params) throws InvalidAlgorithmParameterException
public final void init(AlgorithmParameterSpec params, SecureRandom random) throws InvalidAlgorithmParameterException
~~~

## Parámetros
* **SecureRandom random**,  {% include w3api/param_description.html metodo=_data parametro="SecureRandom random" %}
* **AlgorithmParameterSpec params**,  {% include w3api/param_description.html metodo=_data parametro="AlgorithmParameterSpec params" %}
* **int keysize**,  {% include w3api/param_description.html metodo=_data parametro="int keysize" %}

## Excepciones
[InvalidAlgorithmParameterException](/Java/InvalidAlgorithmParameterException/), [InvalidParameterException](/Java/InvalidParameterException/)

## Clase Padre
[KeyGenerator](/Java/KeyGenerator/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.K.KeyGenerator.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
