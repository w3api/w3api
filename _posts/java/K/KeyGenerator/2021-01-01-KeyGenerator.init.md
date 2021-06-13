---
title: KeyGenerator.init()
permalink: /Java/KeyGenerator/init/
date: 2021-01-11
key: Java.K.KeyGenerator
category: Java
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
* **int keysize**,  {% include w3api/param_description.html metodo=_dato parametro="int keysize" %}
* **AlgorithmParameterSpec params**,  {% include w3api/param_description.html metodo=_dato parametro="AlgorithmParameterSpec params" %}
* **SecureRandom random**,  {% include w3api/param_description.html metodo=_dato parametro="SecureRandom random" %}

## Excepciones
[InvalidParameterException](/Java/InvalidParameterException/), [InvalidAlgorithmParameterException](/Java/InvalidAlgorithmParameterException/)

## Clase Padre
[KeyGenerator](/Java/KeyGenerator/)

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
