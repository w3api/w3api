---
title: Instrument.Instrument()
permalink: /Java/Instrument/Instrument/
date: 2021-01-11
key: Java.I.Instrument
category: Java
tags: ['java se', 'javax.sound.midi', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.Instrument.constructores valor="Instrument" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected Instrument(Soundbank soundbank, Patch patch, String name, Class<?> dataClass)
~~~

## Parámetros
* **String name**,  {% include w3api/param_description.html metodo=_dato parametro="String name" %}
* **Soundbank soundbank**,  {% include w3api/param_description.html metodo=_dato parametro="Soundbank soundbank" %}
* **Class&lt;?&gt; dataClass**,  {% include w3api/param_description.html metodo=_dato parametro="Class<?> dataClass" %}
* **Patch patch**,  {% include w3api/param_description.html metodo=_dato parametro="Patch patch" %}

## Clase Padre
[Instrument](/Java/Instrument/)

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
