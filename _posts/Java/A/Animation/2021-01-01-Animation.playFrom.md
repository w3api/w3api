---
title: Animation.playFrom()
permalink: /Java/Animation/playFrom/
date: 2021-01-11
key: Java.A.Animation
category: Java
tags: ['java se', 'javafx.animation', 'javafx.graphics', 'metodo java', 'JavaFX 2.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.Animation.metodos valor="playFrom" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void playFrom(String cuePoint)
public void playFrom(Duration time)
~~~

## Parámetros
* **String cuePoint**,  {% include w3api/param_description.html metodo=_dato parametro="String cuePoint" %}
* **Duration time**,  {% include w3api/param_description.html metodo=_dato parametro="Duration time" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [IllegalStateException](/Java/IllegalStateException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[Animation](/Java/Animation/)

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
