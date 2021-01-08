---
title: MidiDeviceProvider.getDevice()
permalink: Java/MidiDeviceProvider/getDevice
date: 2021-01-04
key: JavaJava.M.MidiDeviceProvider
category: java
tags: ['java se', 'javax.sound.midi.spi', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.MidiDeviceProvider.metodos valor="getDevice" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract MidiDevice getDevice(MidiDevice.Info info)
~~~

## Parámetros
* **MidiDevice.Info info**,  {% include w3api/param_description.html metodo=_data parametro="MidiDevice.Info info" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[MidiDeviceProvider](/Java/MidiDeviceProvider/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.M.MidiDeviceProvider.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
