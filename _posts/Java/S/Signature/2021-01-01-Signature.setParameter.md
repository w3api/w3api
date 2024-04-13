---
title: Signature.setParameter()
permalink: /Java/Signature/setParameter/
date: 2021-01-11
key: Java.S.Signature
category: Java
tags: ['java se', 'java.security', 'java.base', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.Signature.metodos valor="setParameter" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
@Deprecated public final void setParameter(String param, Object value) throws InvalidParameterException
public final void setParameter(AlgorithmParameterSpec params) throws InvalidAlgorithmParameterException
~~~

## Parámetros
* **AlgorithmParameterSpec params**,  {% include w3api/param_description.html metodo=_dato parametro="AlgorithmParameterSpec params" %}
* **Object value**,  {% include w3api/param_description.html metodo=_dato parametro="Object value" %}
* **String param**,  {% include w3api/param_description.html metodo=_dato parametro="String param" %}

## Excepciones
[InvalidParameterException](/Java/InvalidParameterException/), [InvalidAlgorithmParameterException](/Java/InvalidAlgorithmParameterException/)

## Clase Padre
[Signature](/Java/Signature/)

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
