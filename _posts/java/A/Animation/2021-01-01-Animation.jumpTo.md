---
title: Animation.jumpTo()
permalink: Java/Animation/jumpTo
date: 2021-01-11
key: JavaJava.A.Animation
category: java
tags: ['java se', 'javafx.animation', 'javafx.graphics', 'metodo java', 'JavaFX 2.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.Animation.metodos valor="jumpTo" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void jumpTo(String cuePoint)
public void jumpTo(Duration time)
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
