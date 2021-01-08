---
title: PreferenceChangeEvent.PreferenceChangeEvent()
permalink: Java/PreferenceChangeEvent/PreferenceChangeEvent
date: 2021-01-04
key: JavaJava.P.PreferenceChangeEvent
category: java
tags: ['java se', 'java.util.prefs', 'java.prefs', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.PreferenceChangeEvent.constructores valor="PreferenceChangeEvent" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public PreferenceChangeEvent(Preferences node, String key, String newValue)
~~~

## Parámetros
* **String newValue**,  {% include w3api/param_description.html metodo=_data parametro="String newValue" %}
* **Preferences node**,  {% include w3api/param_description.html metodo=_data parametro="Preferences node" %}
* **String key**,  {% include w3api/param_description.html metodo=_data parametro="String key" %}

## Clase Padre
[PreferenceChangeEvent](/Java/PreferenceChangeEvent/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.P.PreferenceChangeEvent.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
