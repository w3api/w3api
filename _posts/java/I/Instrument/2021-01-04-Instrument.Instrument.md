---
title: Instrument.Instrument()
permalink: Java/Instrument/Instrument
date: 2021-01-04
key: JavaJava.I.Instrument
category: java
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
* **Patch patch**,  {% include w3api/param_description.html metodo=_data parametro="Patch patch" %}
* **Class&lt;?&gt; dataClass**,  {% include w3api/param_description.html metodo=_data parametro="Class<?> dataClass" %}
* **Soundbank soundbank**,  {% include w3api/param_description.html metodo=_data parametro="Soundbank soundbank" %}
* **String name**,  {% include w3api/param_description.html metodo=_data parametro="String name" %}

## Clase Padre
[Instrument](/Java/Instrument/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.I.Instrument.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
