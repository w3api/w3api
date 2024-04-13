---
title: RealmChoiceCallback.RealmChoiceCallback()
permalink: /Java/RealmChoiceCallback/RealmChoiceCallback/
date: 2021-01-11
key: Java.R.RealmChoiceCallback
category: Java
tags: ['java se', 'javax.security.sasl', 'java.security.sasl', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.R.RealmChoiceCallback.constructores valor="RealmChoiceCallback" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public RealmChoiceCallback(String prompt, String[] choices, int defaultChoice, boolean multiple)
~~~

## Parámetros
* **boolean multiple**,  {% include w3api/param_description.html metodo=_dato parametro="boolean multiple" %}
* **String prompt**,  {% include w3api/param_description.html metodo=_dato parametro="String prompt" %}
* **int defaultChoice**,  {% include w3api/param_description.html metodo=_dato parametro="int defaultChoice" %}
* **String[] choices**,  {% include w3api/param_description.html metodo=_dato parametro="String[] choices" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[RealmChoiceCallback](/Java/RealmChoiceCallback/)

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
