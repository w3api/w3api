---
title: AudioPermission.AudioPermission()
permalink: Java/AudioPermission/AudioPermission
date: 2021-01-04
key: JavaJava.A.AudioPermission
category: java
tags: ['java se', 'javax.sound.sampled', 'java.desktop', 'metodo java', 'Java 1.3']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AudioPermission.constructores valor="AudioPermission" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public AudioPermission(String name)
public AudioPermission(String name, String actions)
~~~

## Parámetros
* **String name**,  {% include w3api/param_description.html metodo=_data parametro="String name" %}
* **String actions**,  {% include w3api/param_description.html metodo=_data parametro="String actions" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[AudioPermission](/Java/AudioPermission/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.A.AudioPermission.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
