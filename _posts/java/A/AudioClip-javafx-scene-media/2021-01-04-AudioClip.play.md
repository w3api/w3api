---
title: AudioClip.play()
permalink: Java/AudioClip-javafx-scene-media/play
date: 2021-01-04
key: JavaJava.A.AudioClip-javafx-scene-media
category: java
tags: ['java se', 'javafx.scene.media', 'javafx.media', 'metodo java', 'JavaFX 2.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AudioClip-javafx-scene-media.metodos valor="play" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void play()
public void play(double volume)
public void play(double volume, double balance, double rate, double pan, int priority)
~~~

## Parámetros
* **double volume**,  {% include w3api/param_description.html metodo=_data parametro="double volume" %}
* **double rate**,  {% include w3api/param_description.html metodo=_data parametro="double rate" %}
* **int priority**,  {% include w3api/param_description.html metodo=_data parametro="int priority" %}
* **double pan**,  {% include w3api/param_description.html metodo=_data parametro="double pan" %}
* **double balance**,  {% include w3api/param_description.html metodo=_data parametro="double balance" %}

## Clase Padre
[AudioClip](/Java/AudioClip-javafx-scene-media/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.A.AudioClip-javafx-scene-media.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
