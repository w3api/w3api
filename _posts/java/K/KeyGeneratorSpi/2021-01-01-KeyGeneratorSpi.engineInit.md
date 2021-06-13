---
title: KeyGeneratorSpi.engineInit()
permalink: /Java/KeyGeneratorSpi/engineInit/
date: 2021-01-11
key: Java.K.KeyGeneratorSpi
category: Java
tags: ['java se', 'javax.crypto', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.K.KeyGeneratorSpi.metodos valor="engineInit" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected abstract void engineInit(int keysize, SecureRandom random)
protected abstract void engineInit(SecureRandom random)
protected abstract void engineInit(AlgorithmParameterSpec params, SecureRandom random) throws InvalidAlgorithmParameterException
~~~

## Parámetros
* **int keysize**,  {% include w3api/param_description.html metodo=_dato parametro="int keysize" %}
* **AlgorithmParameterSpec params**,  {% include w3api/param_description.html metodo=_dato parametro="AlgorithmParameterSpec params" %}
* **SecureRandom random**,  {% include w3api/param_description.html metodo=_dato parametro="SecureRandom random" %}

## Excepciones
[InvalidParameterException](/Java/InvalidParameterException/), [InvalidAlgorithmParameterException](/Java/InvalidAlgorithmParameterException/)

## Clase Padre
[KeyGeneratorSpi](/Java/KeyGeneratorSpi/)

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
