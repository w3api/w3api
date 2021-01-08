---
title: ExemptionMechanismSpi.engineGenExemptionBlob()
permalink: Java/ExemptionMechanismSpi/engineGenExemptionBlob
date: 2021-01-04
key: JavaJava.E.ExemptionMechanismSpi
category: java
tags: ['java se', 'javax.crypto', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.E.ExemptionMechanismSpi.metodos valor="engineGenExemptionBlob" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected abstract byte[] engineGenExemptionBlob() throws ExemptionMechanismException
protected abstract int engineGenExemptionBlob(byte[] output, int outputOffset) throws ShortBufferException, ExemptionMechanismException
~~~

## Parámetros
* **byte[] output**,  {% include w3api/param_description.html metodo=_data parametro="byte[] output" %}
* **int outputOffset**,  {% include w3api/param_description.html metodo=_data parametro="int outputOffset" %}

## Excepciones
[ShortBufferException](/Java/ShortBufferException/), [ExemptionMechanismException](/Java/ExemptionMechanismException/)

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
