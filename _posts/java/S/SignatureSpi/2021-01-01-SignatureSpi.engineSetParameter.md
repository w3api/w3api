---
title: SignatureSpi.engineSetParameter()
permalink: /Java/SignatureSpi/engineSetParameter/
date: 2021-01-11
key: Java.S.SignatureSpi
category: Java
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
* **AlgorithmParameterSpec params**,  {% include w3api/param_description.html metodo=_dato parametro="AlgorithmParameterSpec params" %}
* **Object value**,  {% include w3api/param_description.html metodo=_dato parametro="Object value" %}
* **String param**,  {% include w3api/param_description.html metodo=_dato parametro="String param" %}

## Excepciones
[InvalidParameterException](/Java/InvalidParameterException/), [InvalidAlgorithmParameterException](/Java/InvalidAlgorithmParameterException/), [UnsupportedOperationException](/Java/UnsupportedOperationException/)

## Clase Padre
[SignatureSpi](/Java/SignatureSpi/)

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
