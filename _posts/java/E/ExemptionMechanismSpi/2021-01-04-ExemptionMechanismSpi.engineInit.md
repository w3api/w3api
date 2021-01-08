---
title: ExemptionMechanismSpi.engineInit()
permalink: Java/ExemptionMechanismSpi/engineInit
date: 2021-01-04
key: JavaJava.E.ExemptionMechanismSpi
category: java
tags: ['java se', 'javax.crypto', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.E.ExemptionMechanismSpi.metodos valor="engineInit" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected abstract void engineInit(Key key) throws InvalidKeyException, ExemptionMechanismException
protected abstract void engineInit(Key key, AlgorithmParameters params) throws InvalidKeyException, InvalidAlgorithmParameterException, ExemptionMechanismException
protected abstract void engineInit(Key key, AlgorithmParameterSpec params) throws InvalidKeyException, InvalidAlgorithmParameterException, ExemptionMechanismException
~~~

## Parámetros
* **AlgorithmParameters params**,  {% include w3api/param_description.html metodo=_data parametro="AlgorithmParameters params" %}
* **Key key**,  {% include w3api/param_description.html metodo=_data parametro="Key key" %}
* **AlgorithmParameterSpec params**,  {% include w3api/param_description.html metodo=_data parametro="AlgorithmParameterSpec params" %}

## Excepciones
[InvalidKeyException](/Java/InvalidKeyException/), [ExemptionMechanismException](/Java/ExemptionMechanismException/), [InvalidAlgorithmParameterException](/Java/InvalidAlgorithmParameterException/)

## Clase Padre
[ExemptionMechanismSpi](/Java/ExemptionMechanismSpi/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.E.ExemptionMechanismSpi.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
