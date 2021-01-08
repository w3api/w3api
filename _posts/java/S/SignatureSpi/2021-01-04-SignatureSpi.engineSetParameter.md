---
title: SignatureSpi.engineSetParameter()
permalink: Java/SignatureSpi/engineSetParameter
date: 2021-01-04
key: JavaJava.S.SignatureSpi
category: java
tags: ['java se', 'java.security', 'java.base', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SignatureSpi.metodos valor="engineSetParameter" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
@Deprecated protected abstract void engineSetParameter(String param, Object value) throws InvalidParameterException
protected void engineSetParameter(AlgorithmParameterSpec params) throws InvalidAlgorithmParameterException
~~~

## Parámetros
* **String param**,  {% include w3api/param_description.html metodo=_data parametro="String param" %}
* **Object value**,  {% include w3api/param_description.html metodo=_data parametro="Object value" %}
* **AlgorithmParameterSpec params**,  {% include w3api/param_description.html metodo=_data parametro="AlgorithmParameterSpec params" %}

## Excepciones
[InvalidAlgorithmParameterException](/Java/InvalidAlgorithmParameterException/), [UnsupportedOperationException](/Java/UnsupportedOperationException/), [InvalidParameterException](/Java/InvalidParameterException/)

## Clase Padre
[SignatureSpi](/Java/SignatureSpi/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.SignatureSpi.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
