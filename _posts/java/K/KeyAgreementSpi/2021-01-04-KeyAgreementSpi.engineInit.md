---
title: KeyAgreementSpi.engineInit()
permalink: Java/KeyAgreementSpi/engineInit
date: 2021-01-04
key: JavaJava.K.KeyAgreementSpi
category: java
tags: ['java se', 'javax.crypto', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.K.KeyAgreementSpi.metodos valor="engineInit" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected abstract void engineInit(Key key, SecureRandom random) throws InvalidKeyException
protected abstract void engineInit(Key key, AlgorithmParameterSpec params, SecureRandom random) throws InvalidKeyException, InvalidAlgorithmParameterException
~~~

## Parámetros
* **SecureRandom random**,  {% include w3api/param_description.html metodo=_data parametro="SecureRandom random" %}
* **Key key**,  {% include w3api/param_description.html metodo=_data parametro="Key key" %}
* **AlgorithmParameterSpec params**,  {% include w3api/param_description.html metodo=_data parametro="AlgorithmParameterSpec params" %}

## Excepciones
[InvalidKeyException](/Java/InvalidKeyException/), [InvalidAlgorithmParameterException](/Java/InvalidAlgorithmParameterException/)

## Clase Padre
[KeyAgreementSpi](/Java/KeyAgreementSpi/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.K.KeyAgreementSpi.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
