---
title: KeyGeneratorSpi.engineInit()
permalink: Java/KeyGeneratorSpi/engineInit
date: 2021-01-04
key: JavaJava.K.KeyGeneratorSpi
category: java
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
* **SecureRandom random**,  {% include w3api/param_description.html metodo=_data parametro="SecureRandom random" %}
* **AlgorithmParameterSpec params**,  {% include w3api/param_description.html metodo=_data parametro="AlgorithmParameterSpec params" %}
* **int keysize**,  {% include w3api/param_description.html metodo=_data parametro="int keysize" %}

## Excepciones
[InvalidAlgorithmParameterException](/Java/InvalidAlgorithmParameterException/), [InvalidParameterException](/Java/InvalidParameterException/)

## Clase Padre
[KeyGeneratorSpi](/Java/KeyGeneratorSpi/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.K.KeyGeneratorSpi.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
