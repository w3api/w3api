---
title: ConfirmationCallback.ConfirmationCallback()
permalink: Java/ConfirmationCallback/ConfirmationCallback
date: 2021-01-04
key: JavaJava.C.ConfirmationCallback
category: java
tags: ['java se', 'javax.security.auth.callback', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.ConfirmationCallback.constructores valor="ConfirmationCallback" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public ConfirmationCallback(int messageType, int optionType, int defaultOption)
public ConfirmationCallback(int messageType, String[] options, int defaultOption)
public ConfirmationCallback(String prompt, int messageType, int optionType, int defaultOption)
public ConfirmationCallback(String prompt, int messageType, String[] options, int defaultOption)
~~~

## Parámetros
* **String prompt**,  {% include w3api/param_description.html metodo=_data parametro="String prompt" %}
* **int messageType**,  {% include w3api/param_description.html metodo=_data parametro="int messageType" %}
* **String[] options**,  {% include w3api/param_description.html metodo=_data parametro="String[] options" %}
* **int defaultOption**,  {% include w3api/param_description.html metodo=_data parametro="int defaultOption" %}
* **int optionType**,  {% include w3api/param_description.html metodo=_data parametro="int optionType" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[ConfirmationCallback](/Java/ConfirmationCallback/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.C.ConfirmationCallback.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
