---
title: ExemptionMechanism.init()
permalink: Java/ExemptionMechanism/init
date: 2021-01-04
key: JavaJava.E.ExemptionMechanism
category: java
tags: ['java se', 'javax.crypto', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.E.ExemptionMechanism.metodos valor="init" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public final void init(Key key) throws InvalidKeyException, ExemptionMechanismException
public final void init(Key key, AlgorithmParameters params) throws InvalidKeyException, InvalidAlgorithmParameterException, ExemptionMechanismException
public final void init(Key key, AlgorithmParameterSpec params) throws InvalidKeyException, InvalidAlgorithmParameterException, ExemptionMechanismException
~~~

## Parámetros
* **AlgorithmParameters params**,  {% include w3api/param_description.html metodo=_data parametro="AlgorithmParameters params" %}
* **Key key**,  {% include w3api/param_description.html metodo=_data parametro="Key key" %}
* **AlgorithmParameterSpec params**,  {% include w3api/param_description.html metodo=_data parametro="AlgorithmParameterSpec params" %}

## Excepciones
[InvalidKeyException](/Java/InvalidKeyException/), [ExemptionMechanismException](/Java/ExemptionMechanismException/), [InvalidAlgorithmParameterException](/Java/InvalidAlgorithmParameterException/)

## Clase Padre
[ExemptionMechanism](/Java/ExemptionMechanism/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.E.ExemptionMechanism.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
