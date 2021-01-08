---
title: RealmChoiceCallback.RealmChoiceCallback()
permalink: Java/RealmChoiceCallback/RealmChoiceCallback
date: 2021-01-04
key: JavaJava.R.RealmChoiceCallback
category: java
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
* **String[] choices**,  {% include w3api/param_description.html metodo=_data parametro="String[] choices" %}
* **String prompt**,  {% include w3api/param_description.html metodo=_data parametro="String prompt" %}
* **int defaultChoice**,  {% include w3api/param_description.html metodo=_data parametro="int defaultChoice" %}
* **boolean multiple**,  {% include w3api/param_description.html metodo=_data parametro="boolean multiple" %}

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
{%- for _ldc in site.data.Java.R.RealmChoiceCallback.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
