---
title: ExemptionMechanism.genExemptionBlob()
permalink: Java/ExemptionMechanism/genExemptionBlob
date: 2021-01-11
key: JavaJava.E.ExemptionMechanism
category: java
tags: ['java se', 'javax.crypto', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.E.ExemptionMechanism.metodos valor="genExemptionBlob" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public final byte[] genExemptionBlob() throws IllegalStateException, ExemptionMechanismException
public final int genExemptionBlob(byte[] output) throws IllegalStateException, ShortBufferException, ExemptionMechanismException
public final int genExemptionBlob(byte[] output, int outputOffset) throws IllegalStateException, ShortBufferException, ExemptionMechanismException
~~~

## Parámetros
* **byte[] output**,  {% include w3api/param_description.html metodo=_dato parametro="byte[] output" %}
* **int outputOffset**,  {% include w3api/param_description.html metodo=_dato parametro="int outputOffset" %}

## Excepciones
[ShortBufferException](/Java/ShortBufferException/), [IllegalStateException](/Java/IllegalStateException/), [ExemptionMechanismException](/Java/ExemptionMechanismException/)

## Clase Padre
[ExemptionMechanism](/Java/ExemptionMechanism/)

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
