---
title: AudioSystem.getTargetLineInfo()
permalink: Java/AudioSystem/getTargetLineInfo
date: 2021-01-11
key: JavaJava.A.AudioSystem
category: java
tags: ['java se', 'javax.sound.sampled', 'java.desktop', 'metodo java', 'Java 1.3']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AudioSystem.metodos valor="getTargetLineInfo" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static Line.Info[] getTargetLineInfo(Line.Info info)
~~~

## Parámetros
* **Line.Info info**,  {% include w3api/param_description.html metodo=_dato parametro="Line.Info info" %}

## Clase Padre
[AudioSystem](/Java/AudioSystem/)

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