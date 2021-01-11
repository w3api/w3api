---
title: ChoiceCallback.ChoiceCallback()
permalink: Java/ChoiceCallback/ChoiceCallback
date: 2021-01-11
key: JavaJava.C.ChoiceCallback
category: java
tags: ['java se', 'javax.security.auth.callback', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.ChoiceCallback.constructores valor="ChoiceCallback" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public ChoiceCallback(String prompt, String[] choices, int defaultChoice, boolean multipleSelectionsAllowed)
~~~

## Parámetros
* **String prompt**,  {% include w3api/param_description.html metodo=_dato parametro="String prompt" %}
* **boolean multipleSelectionsAllowed**,  {% include w3api/param_description.html metodo=_dato parametro="boolean multipleSelectionsAllowed" %}
* **int defaultChoice**,  {% include w3api/param_description.html metodo=_dato parametro="int defaultChoice" %}
* **String[] choices**,  {% include w3api/param_description.html metodo=_dato parametro="String[] choices" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[ChoiceCallback](/Java/ChoiceCallback/)

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
