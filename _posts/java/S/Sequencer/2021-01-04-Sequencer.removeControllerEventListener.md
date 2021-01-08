---
title: Sequencer.removeControllerEventListener()
permalink: Java/Sequencer/removeControllerEventListener
date: 2021-01-04
key: JavaJava.S.Sequencer
category: java
tags: ['java se', 'javax.sound.midi', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.Sequencer.metodos valor="removeControllerEventListener" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
int[] removeControllerEventListener(ControllerEventListener listener, int[] controllers)
~~~

## Parámetros
* **int[] controllers**,  {% include w3api/param_description.html metodo=_data parametro="int[] controllers" %}
* **ControllerEventListener listener**,  {% include w3api/param_description.html metodo=_data parametro="ControllerEventListener listener" %}

## Clase Padre
[Sequencer](/Java/Sequencer/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.Sequencer.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
