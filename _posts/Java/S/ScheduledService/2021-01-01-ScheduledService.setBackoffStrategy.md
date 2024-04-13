---
title: ScheduledService.setBackoffStrategy()
permalink: /Java/ScheduledService/setBackoffStrategy/
date: 2021-01-11
key: Java.S.ScheduledService
category: Java
tags: ['java se', 'javafx.concurrent', 'javafx.graphics', 'metodo java', 'JavaFX 8.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.ScheduledService.metodos valor="setBackoffStrategy" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public final void setBackoffStrategy(Callback<ScheduledService<?>,Duration> value)
~~~

## Parámetros
* **Callback&lt;ScheduledService&lt;?&gt;**,  {% include w3api/param_description.html metodo=_dato parametro="Callback<ScheduledService<?>" %}
* **Duration&gt; value**,  {% include w3api/param_description.html metodo=_dato parametro="Duration> value" %}

## Clase Padre
[ScheduledService](/Java/ScheduledService/)

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
